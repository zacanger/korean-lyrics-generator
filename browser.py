from browser import document, console
import logic

generate_button = document["generate"]
input_text = document["input"]
output_paragraph = document["output"]


def run_generation(_ev):
    input_lines = input_text.value.strip().split("\n")
    try:
        results = logic.replace_pattern(logic.get_patterns(input_lines))
        output_paragraph.text = ""
        output_paragraph <= results
    except:
        output_paragraph.text = ""
        output_paragraph <= "Error: check your input pattern format!"


document["generate"].bind("click", run_generation)
