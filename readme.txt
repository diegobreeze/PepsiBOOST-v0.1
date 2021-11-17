ESPAÑOL:

¡Este programa solo funciona para WINDOWS 10!
----------------------------------------------

¿Cómo usar el programa?
El programa funciona a través de números los cuales te indica el menú principal. 

¿Es confiable?
Claro que sí, se puede ver el código fuente de todos los archivos (menos .exes)

IMPORTANTE:
Para que el programa funcione correctamente hay que descargar los archivos correspondientes (OPCION 9)

Debes cambiar la ruta en todos los "subprocess.call" después de las comillas simples.
Esto quedaría así:

subprocess.call([r'PATH\\uninstall_apps.bat']) > El nombre del archivo "uninstall_apps.bat" no se debe modificar.

En PATH debe ir:
- Ubicación de disco (ejemplo C:\)
- Carpeta de Usuarios (C:\Users\)
- Usuario (C:\Users\TU USUARIO\)
- Ubicacion de donde esta BOOST.rar (C:\Users\TU USARIO\UBICACION\) Ejemplo: Escritorio, Documentos.
- Quedaría algo así:

C:\Users\TU USUARIO\UBICACION\BOOST\bats\\uninstall_apps.bat

Así se debe remplazar con todos los subprocess que haya.

EJEMPLO:
subprocess.call([r'C:\Users\Pepsi\Desktop\BOOST\bats\\uninstall_apps.bat'])
--------------------------------------------------

CREADOR: https://github.com/UniversePepsi

ENGLISH:

This program only works for WINDOWS 10!

How to use the program?
The program works through numbers which are indicated by the main menu.

Is trustworthy?
Sure, you can see the source code of all files (except .exes)

IMPORTANT:
For the program to work properly, you must download the corresponding files (OPTION 9)

You must change the path in all the "subprocess.call" after the single quotes.
This would look like this:

subprocess.call ([r'PATH\\uninstall_apps.bat'])> The file name "uninstall_apps.bat" must not be modified.

In PATH it should go:
- Disk location (example C:\)
- Users folder (C:\Users\)
- User (C: \Users\YOUR USER\)
- Location where BOOST.rar is (C:\ Users\YOUR USER\LOCATION\) Example: Desktop, Documents.
- It would look something like this:

C: \Users\YOUR USER\LOCATION\BOOST\bats\\uninstall_apps.bat

So it must be replaced with all the subprocesses there are.

EXAMPLE:
subprocess.call ([r'C:\Users\Pepsi\Desktop\BOOST\bats\\uninstall_apps.bat'])

CREATOR: https://github.com/UniversePepsi