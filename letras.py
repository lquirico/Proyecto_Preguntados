import pygame
import pygame.freetype
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Visualización de Fuentes")

# Color de fondo
background_color = (255, 255, 255)
screen.fill(background_color)

# Color del texto
text_color = (0, 0, 0)

# Lista de fuentes
fonts = ['microsoftyibaiti', 'modernno20', 'freesiaupc', 'gillsansultra', 
'arialblack', 'microsofttaile', 'verdana', 'playbill', 'miriamfixed', 
'pristina', 'perpetuatitling', 'helveticaneueltproroman', 'goudystout', 
'ebrima', 'bodoni', 'microsoftjhenghei', 'franklingothicheavy', 'franklingothicmediumcond', 
'microsoftnewtailue', 'garamond', 'utsaah', 'baskervilleoldface', 'bookmanoldstyle', 'couriernew', 
'vani', 'dinprobold', 'moolboran', 'kokilaitali', 'oldenglishtext', 'stencil', 'edwardianscriptitc', 
'script', 'msreferencespecialty', 'franklingothicdemi', 'kalinga', 'segoescript', 'onyx', 
'monotypecorsiva', 'perpetua', 'centaur', 'segoemarker', 'dilleniaupc', 'widelatin', 
'gillsans', 'timesnewroman', 'dinproblack', 'aparajita', 'snapitc', 'berlinsansfbdemi',
'simhei', 'frankruehl', 'harlowsolid', 'cooperblack', 'sylfaen', 'traditionalarabic', 
'freestylescript', 'microsoftsansserif', 'gabriola', 'felixtitling', 'vrinda', 'angsananew', 
'arial', 'lucidacalligraphy', 'impact', 'batangbatangchegungsuhgungsuhche', 'goudyoldstyle', 
'wingdings2', 'showcardgothic', 'erasitc', 'wingdings', 'informalroman', 'twcen', 'comicsansms', 
'aparajitaitali', 'consolas', 'mingliuextbpmingliuextbmingliuhkscsextb', 'kartika', 'segoeui', 'gautami',
'gloucesterextracondensed', 'segoeuisemibold', 'extra', 'californianfb', 'gisha', 
'meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 'copperplategothic', 'plantagenetcherokee', 
'luzsansbook', 'arabictypesetting', 'palacescript', 'juiceitc', 'jokerman', 'bodonipostercompressed',
'tunga', 'niagarasolid', 'simsunextb', 'colonna', 'rockwellcondensed', 'msgothicmspgothicmsuigothic', 
'lucidasansregular', 'franklingothicbook', 'corbel', 'msreferencesansserif', 'rod', 'magneto', 'twcencondensed', 
'rockwell', 'vijaya', 'angsanaupc', 'engravers', 'papyrus', 'bodonicondensed', 'microsofthimalaya', 
'harrington', 'berlinsansfb', 'cambriacambriamath', 'bookantiqua', 'eucrosiaupc', 'franklingothicmedium', 
'segoeprint', 'blackadderitc', 'vinerhanditc', 'kristenitc', 'aharoni', 'jasmineupc', 'lucidasans',
'iskoolapota', 'gulimgulimchedotumdotumche', 'ocraextended', 'microsoftyahei', 'leelawadee', 
'meiryomeiryomeiryouimeiryouiitalic', 'browallianew', 'bauhaus93', 'franklingothicdemicond', 
'simsunnsimsun', 'agencyfb', 'elephant', 'wingdings3', 'sketchflowprint', 'lucidafaxregular',
'narkisim', 'gillsanscondensed', 'laoui', 'webdings', 'chiller', 'kunstlerscript', 'gigi', 'georgia', 
'mingliupmingliumingliuhkscs', 'shruti', 'trajanproregular', 'euphemia', 'lilyupc', 'vladimirscript', 
'mangal', 'bookshelfsymbol7', 'miriam', 'symbol', 'shonarbangla', 'msoutlook', 'curlz', 'calibri', 
'khmerui', 'twcencondensedextra', 'calisto', 'rage', 'bradleyhanditc', 'parchment', 'lucidahandwriting', 
'kokila', 'estrangeloedessa', 'imprintshadow', 'david', 'ravie', 'bodoniblack', 'lucidafax', 'dinprolight',
'erasmediumitc', 'lucidabright', 'dfkaisb', 'gillsansultracondensed', 'poorrichard', 'raavi', 'browalliaupc',
'segoeuisymbol', 'maiandragd', 'lucidasansroman', 'levenim', 'nyala', 'erasdemiitc', 'footlight', 
'malgungothic', 'microsoftuighur', 'candara', 'bell', 'cordiaupc', 'latha', 'castellar', 'mistral',
'andalus', 'lucidasanstypewriteroblique', 'trebuchetms', 'lucidaconsole', 'fangsong', 'swtortrajan',
'daunpenh', 'century', 'forte', 'bernardcondensed', 'sakkalmajalla', 'niagaraengraved', 'broadway',
'vivaldi', 'arialrounded', 'gillsansextcondensed', 'tahoma', 'arialms', 'haettenschweiler', 'dinproregular',
'buxtonsketch', 'simplifiedarabic', 'britannic', 'centuryschoolbook', 'centurygothic', 'cambria', 'brushscript',
'mvboli', 'hightowertext', 'cordianew', 'kaiti', 'rockwellextra', 'msmincho', 'utsaahitali',
'simplifiedarabicfixed', 'microsoftphagspa', 'dokchampa', 'constantia', 'lucidasanstypewriterregular', 
'kodchiangupc', 'palatinolinotype', 'lucidasanstypewriter', 'algerian', 'mongolianbaiti', 'irisupc', 
'maturascriptcapitals', 'dinpromedium', 'frenchscript', 'msminchomspmincho', 'tempussansitc']

# Número de fuentes por página
fonts_per_page = 20
total_pages = len(fonts) // fonts_per_page + (1 if len(fonts) % fonts_per_page > 0 else 0)
current_page = 0

def render_fonts(page):
    screen.fill(background_color)
    y = 20
    start_index = page * fonts_per_page
    end_index = start_index + fonts_per_page
    for font_name in fonts[start_index:end_index]:
        try:
            font = pygame.freetype.SysFont(font_name, 24)
            font.render_to(screen, (20, y), f"Ejemplo de texto en la fuente: {font_name}", text_color)
            y += 30
        except:
            print(f"Fuente {font_name} no encontrada en el sistema.")
    pygame.display.flip()

# Renderiza la primera página
render_fonts(current_page)

# Mantiene la ventana abierta hasta que el usuario la cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and current_page < total_pages - 1:
                current_page += 1
                render_fonts(current_page)
            elif event.key == pygame.K_LEFT and current_page > 0:
                current_page -= 1
                render_fonts(current_page)

pygame.quit()
sys.exit()
