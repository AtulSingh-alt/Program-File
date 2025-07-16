# phone_no = {'Ram':1234, 'Shyam':3456, 'Mohan':8976}
# print(phone_no)
#
# phone_no['Mohan']=9999
# print(phone_no)
# phone_no['Madhav']={1111,2222,3333}
# print(phone_no)
# phone_no['Shyam']={'Shyam_Home':5555,'Shyam_work':4444}
# print(phone_no)
# print(phone_no['Shyam'])
# print(phone_no['Shyam']['Shyam_work'])
# or
# print(phone_no.pop('Shyam'))
# print(phone_no.popitem())
# print(phone_no.clear())
# print(phone_no.keys())
# print(phone_no.values())
# print(phone_no.items())
# phone_no2=phone_no.copy()
# print(phone_no2)
# print(len(phone_no))
# data={
#     1:'Jenny',
#     2:'Ram',
#     0:'Mohan'
# }
#
# print(data[0])
# for i in phone_no:
#     print(i)
#     print(phone_no[i])


# #Nested Dictionary
# student_data={
#     "Ram":{"roll_no":10, "age":20,"course":"Python"},
#     "Mohan":{"roll_no":20,"age":22,"course":"Java"}
# }
# print(student_data["Mohan"])
# print(student_data["Mohan"]["roll_no"])
# student_data["Mohan"]["Phone_no"]=97987
# print(student_data["Mohan"])
# # del student_data["Mohan"]["Phone_no"]
# print(student_data["Mohan"].pop("Phone_no"))
# print(student_data["Mohan"])

# Program
# student_marks ={
#     "Atul":96,
#     "Sunny":87,
#     "Dimpy":56,
#     "Rahul":47,
#     "Shubh":81
# }
# student_grades={}
# for student in student_marks:
#     marks=student_marks[student]
#     if marks>90:
#         student_grades[student]="A+"
#     elif marks>80:
#         student_grades[student]="A"
#     elif marks>70:
#         student_grades[student]="B+"
#     elif marks>60:
#         student_grades[student]="B"
#     else:
#         student_grades[student]="F"
# print(student_grades)

#nesting of list withing a dictionary
# travel_data={
#     "Gujrat":["Dwarkadhish","Somnath","Statue of Unity"],
#     "Rajsthan":["Jaipur","Udaipur"]
# }
# print(travel_data)

#nesting of dictionary within a list
# student_data=[
#     {"Name":"Ram","Roll_no":10,"age":20,"course":"Python"},
#     {"Name":"Mohan","roll_no":20,"age":22,"course":"Java","Phone_no":[8979,456576]}
# ]
# print(student_data)
# print(student_data[1]["Phone_no"])

#Program
# student_data=[
#     {
#         "Name":"Ram",
#         "roll_no":10,
#         "age":20,
#         "course":"Python"
#     },
#     {
#         "Name":"Mohan",
#         "roll_no":20,
#         "age":22,
#         "course":"Java"
#     }
# ]
# def add_new_student(name,rollno,age,course_opted):
#     new_student={}
#     new_student["Name"]=name
#     new_student["roll_no"]=rollno
#     new_student["age"]=age
#     new_student["course"]=course_opted
#     student_data.append(new_student)
#
# add_new_student("Shyam",23,24,"C++")
# print(student_data)

#Program for Silent Auction
import os
print("******Welcome to the Silent Auction Program*******")
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"Here is the list of all the bidders:{bidder_details}")
    print(f"The winner is {winner} with a bid price of {highest_bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name= input("What is your name?: ")
    price= int(input("What is your bid?: "))
    bidder_data[name]=price
    more_bidders= input("Are there more bidders? Type 'yes' or 'no'").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
