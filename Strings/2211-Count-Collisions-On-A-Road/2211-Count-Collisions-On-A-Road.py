class Solution:
    def countCollisions(self, directions: str) -> int:
        while(directions and directions[-1]=='R'):
            directions=directions[:-1]
            
        while directions and directions[0]=='L':
            directions=directions[1:]
            
        print("final",directions)
        return len(directions)-directions.count('S')
