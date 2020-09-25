extends RigidBody2D

var a = 2 # ha változót létre szeretnénk hozni akkor ezt a var segítségével tudjunk megadni, majd utána egy nevet adunk (let a =) scoolcodeban.
var b = false # logikai változó (lehet true, false) igaz vagy hamis
const e = 5 # konstans változó (különbség az lesz, hogy míg a var-t bármikor átírhatom kedvem szerint, míg itt mindig fix érték fog szerepelni.)

var speed:int = 1000 # var speed, (nincs típusa, de ezt meg tudjuk adni a következő módon) - sebességet fog eltárolni : után meadjuk a típusát h pl int [integer] (egész számok).
var canJump:bool = true # tudunk e ugrani? igen/nem logikai változó (boolean) - bool
const velo:String = "alma" # amennyiben szöveget szeretnénk azt stringként tudjuk tárolni.

var Name = "Patrik Kis"
var Born = "1998.06.23"
var City = "Budapest"
var Prog = "programozás"
# Called when the node enters the scene tree for the first time.
func _ready():
	print("Hello Logiscool!")
	print(Name)
	print(Born)
	print(City)
	
	print("Szia, én "+Name+" vagyok,"+City+"-en születtem. Kedvenc időtöltésem a: "+Prog+"")
	
	#Draw
	print("     /\\      ")
	print("    /  \\     ")
	print("   /    \\    ")
	print("  /      \\   ")
	print(" /        \\  ")
	print("/__________\\ ")
	
	print("-------------------")
	#Loops
	for x in range(5):
		print(x)
	print("-------------------")
	for y in range(2,10):
		print(y)
	print("-------------------")
	for z in range(2,10,2):
		print(z)

var countNumber = 0
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	#print(countNumber)
	countNumber += 1 * delta
