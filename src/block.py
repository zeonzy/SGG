

def markdown_to_blocks(markdown):
    #first plits into individual lines and strips leading and trailing whitspaces
    output = []
    for block in "\n".join((map(lambda x: x.strip(), markdown.split("\n")))).split("\n\n"):
        #filter out any empty double enters
        if block != "":
            sub_output = []
            #filter out any empty enters while keeping the block markup
            for sub_block in block.split("\n"):
                if sub_block != "":
                    sub_output.append(sub_block)
            output.append("\n".join(sub_output))
    return output

