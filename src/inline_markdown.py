from textnode import TextNode,TextType

        
def split_nodes_delimiter(old_nodes, delimiter, text_type):   
    if not delimiter:
        raise Exception("Invalid Markdown syntax")
   
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        elif node.text_type is TextType.TEXT:
            s_node = node.text.split(delimiter)
            if len(s_node) > 1 and len(s_node) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            for i, n in enumerate(s_node):
                if n == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(n,TextType.TEXT))
                else:
                    new_nodes.append(TextNode(n,text_type))
    return new_nodes

