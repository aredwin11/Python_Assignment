from util import generate_h_logo

if __name__ == '_main_':
    thickness = int(input("Enter an odd number for thickness: "))
    logo = generate_h_logo(thickness)
    for line in logo:
        print(line)