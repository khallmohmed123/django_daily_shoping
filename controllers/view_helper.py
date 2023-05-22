class items:
    def open_li(li_class="",style="",params=""):
        return "<li class='{}' style='{}' {}>".format(li_class,style,params)
    def a(href="",a_class="",style="",params="",content=""):
        return "<a href='{}' class='{}' style='{}' {}>{}</a>".format(href,a_class,style,params,content)
    def span(span_class="",style="",params="",content=""):
        return "<span class='{}' style='{}' {}>{}</span>".format(span_class,style,params,content)
    def open_ul(ul_class="",style="",params=""):
        return "<ul class='{}' style='{}' {}>".format(ul_class,ul_class,params)
    def colse_li():
        return "</li>"
    def close_a():
        return "</a>"
    def close_ul():
        return "</ul>"
