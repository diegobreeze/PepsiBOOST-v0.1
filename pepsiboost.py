"""
Creator: Pepsi (elpepsireal).
GitHub: https://github.com/UniversePepsi
Version: 0.1

READ readme.txt!
"""

# Imports
import os, subprocess, time, ctypes, sys, webbrowser, winreg

# Admin function
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Set windows optimizations (reg)
def set_windows_path_var(self, value):
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:
            with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", 0, winreg.REG_EXPAND_SZ, value)

        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A

        SMTO_ABORTIFHUNG = 0x0002

        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(
            HWND_BROADCAST,
            WM_SETTINGCHANGE,
            0,
            u"Environment",
            SMTO_ABORTIFHUNG,
            5000,
            ctypes.byref(result),
        ) 

# Colors
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[;36m' 
    RESET = '\033[0m'

# Status of process
STATUS_OK = bcolors.GREEN + 'STATUS: [OK]' + bcolors.RESET

# Check privileges
if is_admin():
    os.system('cls')
    print(bcolors.GREEN + '[----------------------------------]')
    print('     P E P S I - B O O S T v0.1   ')     
    print('[----------------------------------]\n' + bcolors.RESET)

    print(bcolors.CYAN + '[1]: Open windows bats\n[2]: Disable hibernation\n[3]: Windows Optimizations (reg)\n[4]: Clear all temporal files')
    print('[5]: Open DWS_2.exe\n[6]: Open killer.bat\n[7]: Set max power plan.\n[8]: Cleaning files (CCleaner, etc)\n[9]: Download all files\n' + bcolors.RESET)

    option = int(input(bcolors.RED + '[>] Introduce an option: '))
    os.system('cls')

    # Alghoritm 
    while option >= 1 and option <= 9:
        if option == 1:
            # Uninstalling uneccesary apps
            print ('[>] Uninstalling unnecessary applications...')
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\uninstall_apps.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[1]: ' + STATUS_OK)
            time.sleep(1)
        
            # Hiding one drive
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\hide_onedrive.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[2]: ' + STATUS_OK)
            time.sleep(1)
        
            # Putting advanced settings on Windows
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\advanced_settings.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[3]: ' + STATUS_OK)
            time.sleep(1)
        
            # Disabling automatic updates
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\disable_update.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[4]: ' + STATUS_OK)
            time.sleep(1)
        
            # Disabling cortana
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\disable_cortana.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[5]: ' + STATUS_OK)
            time.sleep(1)
        
            # Disabling automatic reboot
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\disable_restart.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[6]: ' + STATUS_OK)
            time.sleep(1)
        
            # Disabling lockscreen
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\disable_lockscreen.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[7]: ' + STATUS_OK)
            time.sleep(1)
        
            # Disabling telemetry
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\disable_telemetry.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[8]: ' + STATUS_OK)
            time.sleep(1)
        
            # Disabling uneccesary services
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\disable_services.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[9]: ' + STATUS_OK)
            time.sleep(1)
        
            # Hiding cortana
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\hide_cortana.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[10]: ' + STATUS_OK)
            time.sleep(1)
        
            print('[Option 1]: FINISHED! Thanks for using.')
            time.sleep(2)
            break
    
        if option == 2:
            print(bcolors.GREEN + '[>] Disabling hibernation..')
            # Disabling hibernation
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\dwsespias\\disable_hibernation.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[>] HIBERNATION: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 2]: FINISHED! Thanks for using.')
            break
    
        if option == 3:
            # Setting regedit optimizations
            print(bcolors.GREEN + '[>] Loading windows optimizations (regedit)')
            os.system('cls')
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', '"NetworkThrottlingIndex"=dword:ffffffff')
            
            print(bcolors.RED + '[1]: NetworkThrottlingIndex (VALUE; dword:ffffffff): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', '"SystemResponsiveness"=dword:00000000')
            
            print(bcolors.RED + '[2] SystemResponsiveness (VALUE: dword:00000000): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling', '"PowerThrottlingOff"=dword:00000001')
            
            print(bcolors.RED + '[3] PowerThrottlingOff (VALUE: dword:00000001): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\PriorityControl', '"Win32PrioritySeparation"=dword:00000026')
            
            print(bcolors.RED + '[4] Win32PrioritySeparation (VALUE: dword:00000026): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"Affinity"=dword:00000000')
            
            print(bcolors.RED + '[5] Affinity (VALUE: dword:00000000): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"Background Only"="False"')
            
            print(bcolors.RED + '[6] Background Only (VALUE: False): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"Clock Rate"=dword:00002710')
            
            print(bcolors.RED + '[7] Clock Rate (VALUE: dword:00002710): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"GPU Priority"=dword:00000008')
            
            print(bcolors.RED + '[8] GPU Priority (VALUE: dword:00000008): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"Priority"=dword:00000006')
            
            print(bcolors.RED + '[9] Priority (VALUE: dword:00000006): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"Scheduling Category"="High"')
            
            print(bcolors.RED + '[10] Scheduling Category (VALUE: High): ' + STATUS_OK)
            time.sleep(1)
            
            set_windows_path_var('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games', '"SFIO Priority"="High"')
            
            print(bcolors.RED + '[11] SFIO Priority (VALUE: High): ' + STATUS_OK)
            time.sleep(1)
            print('[Option 3]: FINISHED! Thanks for using.')
            break
    
        if option == 5:
            print(bcolors.GREEN + '[>] Opening DWS_2.exe...')
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\dwsespias\\DWS_2.exe']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[>] DWS_2: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 5]: FINISHED! Thanks for using.')
            break
    
        if option == 4:
            print(bcolors.GREEN + '[>] Clearing all Temporal Files of your PC!')
            # Clearing temporally files!
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\dwsespias\\TR.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[>] Temporal files: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 4]: FINISHED! Thanks for using.')
            break
    
        if option == 6:
            print(bcolors.GREEN + '[>] Opening killer.bat...')
            # Killing processes so as not to intervene in adjustments
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\\killer.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[>] Killing PROCESS: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 6]: FINISHED! Thanks for using.')
            break
        
        if option == 7:
            print('[>] Applying the best energy plan...')
            # Best power plan for Windows (duplicatesheme)
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\\power.bat']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[>] Best power plan: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 7]: FINISHED! Thanks for using.')
            break
    
        if option == 8:
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\\limpieza\\ccleaner.exe']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[1]: Opening CCleaner: ' + STATUS_OK)
            time.sleep(1)
        
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\\limpieza\\mbytes.exe']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[2]: Opening MalwareBytes: ' + STATUS_OK)
            time.sleep(1)
        
            subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\\limpieza\\processlasso.exe']) # CHANGE AT YOUR PATH
            os.system('cls')
        
            print(bcolors.RED + '[3]: Opening ProcessLasso: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 8]: FINISHED! Thanks for using.')
            break

        if option == 9:
            # Opening files to download in a new tab
            print(bcolors.RED + '[>] Opening ' + bcolors.GREEN + 'https://www.mediafire.com/file/twefd0h4bk27ah3/BOOST.rar/file')
            webbrowser.open_new_tab('https://www.mediafire.com/file/twefd0h4bk27ah3/BOOST.rar/file')
            os.system('cls')
                        
            print(bcolors.RED + '[>] WebSite: ' + STATUS_OK)
            time.sleep(1)
            print('[Option 9]: FINISHED! Thanks for using.')
            break
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)