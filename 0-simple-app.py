import justpy as jp

def app():
    wp = jp.QuasarPage()
    d1 = jp.QDiv(a=wp , text='Analysis of course review' , classes='text-h3 text-center')
    p1 = jp.QDiv(a=wp , text='these graphs represents course analysis review')
    return wp
jp.justpy(app)



