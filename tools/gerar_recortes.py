# Gera os recortes reais das duas capas. Uso (na raiz do projeto): python3 -I tools/gerar_recortes.py
# Capa única: assets/cover.jpg (capa branca, p&b, 300 px). A foto colorida usada nas listras já foi convertida em assets/listras.jpg.
import numpy as np
from PIL import Image
dia = Image.open('assets/cover.jpg').convert('RGB')
dia.resize((256, 256), Image.LANCZOS).save('assets/cover-256.jpg', quality=88)
dia.resize((512, 512), Image.LANCZOS).save('assets/cover-512.jpg', quality=90)

def mascara(img, box, saida, esc=4, ruido=6, gama=75):
    """alfa = quanto cada pixel é mais escuro que o fundo claro da capa (as letras do logo)"""
    x0, y0, x1, y1 = box
    l = np.asarray(img.crop(box).convert('L')).astype(float)
    bg = np.percentile(l, 97)
    a = np.clip((bg - l - ruido) / gama, 0, 1)
    a[a < 0.10] = 0
    out = np.zeros(l.shape + (4,), np.uint8); out[..., 3] = (a * 255).astype(np.uint8)
    Image.fromarray(out, 'RGBA').resize(((x1 - x0) * esc, (y1 - y0) * esc), Image.LANCZOS).save(saida, quality=92)

mascara(dia, (32, 16, 118, 47), 'assets/logo-dia.webp')        # logo na capa p&b

