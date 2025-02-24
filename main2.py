Amount=int(input("Enter the amount that you wish to withdraw: "))

note_1000=Amount//1000
note_500=(Amount%1000)//500
note_200=((Amount%1000)%500)//200
note_100=(((Amount%1000)%500)%200)//100
note_50=((((Amount%1000)%500)%200)%100)//50
note_25=(((((Amount%1000)%500)%200)%100)%50)//25

print("The total number of notes for 1000 notes is ",note_1000)
print("The total number of notes for 500 notes is ",note_500)
print("The total number of notes for 200 notes is ",note_200)
print("The total number of notes for 100 notes is ",note_100)
print("The total number of notes for 50 notes is ",note_50)
print("The total number of notes for 25 notes is ",note_25)
