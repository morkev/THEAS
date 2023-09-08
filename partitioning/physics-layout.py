import math


def norm(x, y):
    return math.sqrt(x*x + y*y)


class PhysicsLayout(object):

    def __init__(self, damping=0.1, verbose=False, max_steps=50, bounds=None):
        self.damping = damping
        self.verbose = verbose
        self.max_steps = max_steps
        self._reset()

        if bounds:
            self.bounds = bounds
            self._create_bounds()

    def add_edge(self, id_a, id_b, weight, fixed=False):
        hz = 20 + 20.0 * weight
        dr = .4
        bodyA = self.bodies[id_a]
        bodyB = self.bodies[id_b]
        joint = self.world.CreateDistanceJoint(
            frequencyHz=hz,
            dampingRatio=dr,
            bodyA=bodyA,
            bodyB=bodyB,
            length=bodyA.userData['r'] + bodyB.userData['r'],
            collideConnected=True,
            userData={'weight': weight}
        )

    def add_hard_edge(self, id_a, id_b):
        bodyA = self.bodies[id_a]
        bodyB = self.bodies[id_b]
        length = bodyA.userData['r'] + bodyB.userData['r']
        joint = self.world.CreateRopeJoint(
            bodyA=bodyA,
            bodyB=bodyB,
            maxLength=length,
            localAnchorA=(0, 0),
            localAnchorB=(0, 0),
            # collideConnected=True,
        )

    def _applyGravity(self):
        cx = 0  # self.bounds[0]/2.
        cy = 0  # self.bounds[1]/2.

        for body in self.world.bodies:
            cx += body.position[0]
            cy += body.position[1]
        cx /= len(self.world.bodies)
        cy /= len(self.world.bodies)

        for body in self.world.bodies:
            x = body.position[0] - cx
            y = body.position[1] - cy
            l = norm(x, y)
            if l != 0:
                f = (-(x/l)*body.mass*1000, -(y/l)*body.mass*1000)
                body.ApplyForce(f, (0, 0), True)

    def cool(self):
        cool = 1 - (self.steps / float(self.max_steps))
        for body in self.world.bodies:
            body.linearVelocity *= cool

    def run(self, view=None):
        timeStep = 1.0 / 120.
        vel_iters, pos_iters = 100, 100

        for step in range(self.max_steps):
            # if step%5 == 0:
            #     print(sum(b.linearVelocity[0] for b in self.world.bodies))
            self._applyGravity()
            self.world.Step(timeStep, vel_iters, pos_iters)
            # self.cool()
            if view is not None:
                view.draw_physics_layout(self)

            if view and step == 0:
                view.save('temp1.png')

            self.steps += 1

        if view:
            view.save('temp%i.png' % self.steps)
