# The "Food" class

class Food():

    def __init__(self, position, tileSize):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.position = position
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.tileSize = tileSize

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(255, 0, 0)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x + self.tileSize/2, self.position.y + self.tileSize/2)
            rotate(theta)
            circle(0, 0, self.r)
            
