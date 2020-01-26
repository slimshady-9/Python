class duck:
    def swim(self):
        print("It swims");
    def walk(self):
        print("It walks");
    def sound(self):
        print("It hjonks");

class frog():
    def swim(self):
        print("It swims");
    def walk(self):
        print("It walks");  
    def sound(self):
        print("It croaks");

class fish():
    def swim(self):
        print("It swims");

class elephant():
    def walk(self):
        print("It walks");  
    def sound(self):
        print("It trumps -_-");

def duckwalk(self):
    self.walk();
def duckswim(self):
    self.swim();
def ducksound(self):
    self.sound();

def main():
    Duck=duck();
    Frog=frog();
    Fish=fish();
    Elephant=elephant();
   
    duckwalk(Duck);
    duckwalk(Frog);
    duckwalk(Elephant);

    duckswim(Frog);
    duckswim(Duck);
    duckswim(Fish);
   
    ducksound(Frog);
    ducksound(Duck);
    ducksound(Elephant);

main();
