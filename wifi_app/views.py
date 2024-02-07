import wifi
from django.shortcuts import render

def home(request):
    available_wifis = get_available_wifis()
    context = {'wifis': available_wifis}
    return render(request, 'home.html', context)

def connect(request, wifi_name):
    # You can implement the connection logic here (not recommended for security reasons)
    # For demonstration purposes, let's assume a successful connection
    success_message = f"Connected to {wifi_name} successfully!"
    context = {'success_message': success_message}
    return render(request, 'connect.html', context)

def get_available_wifis():
    # Use the wifi library to get available Wi-Fi SSIDs
    available_wifis = [cell.ssid for cell in wifi.Cell.all('wlp0s20f3')]
    return available_wifis
