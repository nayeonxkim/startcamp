def play(self, F):
    self.balls[0].getforce(F)
    cnt = 0
    while self.checkrestballs():
        cnt += 1
        col_group = self.checkcollisionballs()

        for b1, b2 in col_group:
            b1.vel, b2.vel = elastic_collision(b1, b2)

        for ball in self.balls:
            ball.update()
            isout(ball)
            # print(ball.vel, ball.pos)