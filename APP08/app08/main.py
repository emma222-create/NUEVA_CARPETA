import flet as ft


def main(page: ft.Page):


    page.window_width=800
    page.window_height=800

    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="blue"
    
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    PrimerNivel=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(PrimerNivel)
    
    segundoNivel=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(segundoNivel)
    
    tercerNivel=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(tercerNivel)
    
    cuartoNivel=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(cuartoNivel)
    
    QuintoNivel=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(QuintoNivel)
    
    SextoNivel=ft.Audio(src="Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(SextoNivel)
    
    SeptimoNivel=ft.Audio(src="Septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(SeptimoNivel)
    
    OctavoNivel=ft.Audio(src="Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(OctavoNivel)
    
    NovenoNivel=ft.Audio(src="Noveno_Nivel.mp3"volume=1,balance=0)
    page.overlay.append(NovenoNivel)

#Se crea la interfaz

    btnIntro=ft.FilledButton(text="Escucha el Intro", diasabled=False)
    
    btnNivel1=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg", width=150,height=150)
    
    btnNivel2=ft.ElevatedButton(text="Segundo Nivel")
    img2=ft.Image(src="Segundo -Nivel.jpeg",width=150,height=150)
    
    btnNivel3=ft.ElevatedButton(text="Tercer Nivel")
    img3=ft.Image(src="Tercer-Nivel.png",width=150,height=150)
    
    btnNivel4=ft.ElevatedButton(text="Cuarto Nivel")
    img4=ft.Image(src="Cuarto-Nivel.jpeg",width=150,height=150)
    
    btnNivel5=ft.ElevatedButton(text="Quinto Nivel")
    img5=ft.Image(src="Quinto_Nivel.")
    
    
    page.add(
        ft.Row()
            alignment="start",
        ),
        ft.Column(
            alignment="Center"
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="Center",
                    controls=[btnNivel1,img1]
                ),
            ]
        )
    
    
    
    
    
    
ft.app(main)
