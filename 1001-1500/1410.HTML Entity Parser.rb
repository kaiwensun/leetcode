# @param {String} text
# @return {String}
def entity_parser(text)
    trans = [
        ["&quot;", '"'],
        ["&apos;", "'"],
        ["&gt;", ">"],
        ["&lt;", "<"],
        ["&frasl;", "/"],
        ["&amp;", "&"]
    ]
    trans.each { |tr| text.gsub! tr[0], tr[1] }
    text
end
