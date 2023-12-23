from django.shortcuts import render
import serial
import time

ser = serial.Serial("COM7", 9600)
def getDataApp(request):
    if request.method == "POST":
        try:
            a = str(request.POST["datafield"])
            ser.write(a.encode())
            print(a)
            time.sleep(2)
        except:
            print("error")
    # ser.close()
    return render(request, "indexform.html")

# import serial
# import time
# from django.shortcuts import render

# # Initialize the serial connection outside the view
# ser = serial.Serial("COM7", 9600)

# def getDataApp(request):
#     if request.method == "POST":
#         try:
#             a = str(request.POST["datafield"])
#             ser.write(a.encode())
#             print(a)
#             time.sleep(2)
#         except Exception as e:
#             print("Error:", e)

#     return render(request, "indexform.html")
