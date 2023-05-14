import sys
import config

example_items = []
max_num_of_print = 5
search_term = "---"

class Example:

   path = "-"
   description = "-"
   src_example = "-"
   point = 0

   def compute_point(self, search_term):
      desc_pos = self.description.find(search_term)
      ex_pos = self.src_example.find(search_term)

      if (-1 < desc_pos) or (-1 < ex_pos):
         self.point = self.point + 10

         desc_words = self.description.split()
         ex_words = self.src_example.split()

         if search_term in desc_words:
            self.point = self.point + 10

         if search_term in ex_words:
            self.point = self.point + 10

   def __repr__(self):
      return "[" + self.description + ", " + self.src_example + ", " + str(self.point) + "]"

def load_examples(source_path):
    f = open(source_path, "r")

    for line in f:
      if line.startswith("*"):
         ex = Example()
         ex.description = line[2:-1]
         example_items.append(ex)

      if line.startswith("`"):
         if example_items[-1].src_example == "-":
            example_items[-1].src_example = line[1:-2]

def sort_examples(search_term):

   for ex in example_items:
      ex.compute_point(search_term)

   example_items.sort(reverse = True, key=lambda example: example.point)

def print_results():
   for ex in example_items[0:max_num_of_print]:
      if (0 < ex.point):
         print("> " + ex.description)
         print(ex.src_example)
      else:
         break

def load_all_sources():
   for s in config.source_files:
      load_examples(s)

def process_arguments():
   global max_num_of_print
   global search_term

   if "-n" == sys.argv[1]:
      max_num_of_print = int(sys.argv[2])
      search_term = sys.argv[3]
   else:
      search_term = sys.argv[1]

process_arguments()
load_all_sources()
sort_examples(search_term)
print_results()
