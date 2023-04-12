import atheris
import sys

import dictgen

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    rand_max_height = fdp.ConsumeIntInRange(-100,100)
    rand_max_depth = fdp.ConsumeIntInRange(-100,100)
    rand_seed = fdp.ConsumeIntInRange(-1000000,1000000)
    # print(f"{rand_max_height} {rand_max_depth} {rand_seed}")
    try:
      generated_dict = dictgen.generate(max_height=rand_max_height, max_depth=rand_max_depth, rand_seed=rand_seed)
      if dictgen.max_depth(generated_dict) > rand_max_depth:
        raise f"Dictionary of depth {dictgen.max_depth(generated_dict)} generated for {rand_max_depth}"
      if dictgen.max_height(generated_dict) > rand_max_height:
          raise f"Dictionary of depth {dictgen.max_height(generated_dict)} generated for {rand_max_height}"
    except (AttributeError):
       pass

def main():
  atheris.instrument_all()
  atheris.Setup(sys.argv, TestOneInput)
  atheris.Fuzz()

if __name__ == "__main__":
  main()