import jinja2
import pdfkit

def crea_pdf(info, rutacss=''):
    ruta_template = './template1'
    nombre_template = 'index.html'

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    opciones = {'page-size': 'Letter',
                'encoding': "UTF-8",
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                # 'footer-center': '[page] of [topage]',
                # 'footer-line': '',
    }

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    ruta_salida = 'cotizacion.pdf'

    pdfkit.from_string(html, ruta_salida, options=opciones, configuration=config)

if __name__ == '__main__':
    info = {
        'data': [
            {'producto': 'IMPRESORA EPSON L1250, PPM 33 NEGRO 15 COLOR, TINTA CONTINUA, ECOTANK', 'cantidad': 10}, 
            {'producto': 'KIT 11 GEN BOARD MSI B560M- PRO + CELERON G5905 3.5 GHz + 4GB MEMORIA RAM', 'cantidad': 15}, 
                ]
    }

    crea_pdf(info)