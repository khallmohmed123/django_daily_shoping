from controllers.view_helper import *
from categories.models import Category
import re

def load_featured_products():
    items_node_array=[]
    categories = Category.objects.filter(is_parent=1)
    for i in categories:
        nodes_str=""
        items_node_array.append(items.open_li()+items.a(href="{}/category/{}".format("http://192.168.33.180",i.id),content="{} {}".format(i.name,items.span(span_class="caret"))))
        recurse(i.id,node_str=items_node_array)
        items_node_array.append(items.colse_li())
    return items_node_array
def recurse(id,node_str):
    try:
        sub=Category.objects.filter(parent_id=id).all()
        if len(sub) == 0 :
            pattern = "<[ ]*span.*class=.*caret.*span[ ]*>"
            string_val=node_str[-1]
            string_val = re.sub(pattern,"",string_val)
            node_str[-1]=string_val
            raise(Category.DoesNotExist)
        node_str.append(items.open_ul(ul_class="dropdown-menu"))
        for i in sub:
            node_str.append(items.open_li()+items.a(href="{}/category/{}".format("http://192.168.33.180",i.id),content="{} {}".format(i.name,items.span(span_class="caret"))))
            recurse(i.id,node_str)
            node_str.append(items.colse_li())
        node_str.append(items.close_ul())
    except Category.DoesNotExist:
        return ""
    except:
        return ""
    return node_str