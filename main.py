from rembg import remove
import sys

def rem_bg(input_path, output_path, model_path):
        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input,model_path=model_path)
                o.write(output)
if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    model_path = sys.argv[3]
    rem_bg(input_path, output_path, model_path)



