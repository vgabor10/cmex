import sys

example_items = []
max_num_of_print = 5
search_terms = []
source_files = []

class Example:

   path = "-"
   description = "-"
   src_example = "-"
   point = 0

   def update_point_for_a_search_word(self, search_word):
      desc_pos = self.description.find(search_word)
      ex_pos = self.src_example.find(search_word)

      if (-1 < desc_pos) or (-1 < ex_pos):
         self.point = self.point + 10

         desc_words = self.description.split()
         ex_words = self.src_example.split()

         if search_word in desc_words:
            self.point = self.point + 10

         if search_word in ex_words:
            self.point = self.point + 10

   def compute_full_point(self):
      global search_terms

      for search_word in search_terms:
         self.update_point_for_a_search_word(search_word)

      if (20 > len(self.src_example)):
        self.point + 5
      elif (30 > len(self.src_example)):
        self.point + 4
      elif (40 > len(self.src_example)):
        self.point + 3
      elif (50 > len(self.src_example)):
        self.point + 2
      elif (60 > len(self.src_example)):
        self.point + 1

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

def sort_examples():

   for ex in example_items:
      ex.compute_full_point()

   example_items.sort(reverse = True, key=lambda example: example.point)

def print_results():
   for i in range(0, min(max_num_of_print, len(example_items))):
      if (0 < example_items[i].point):
         print("> " + example_items[i].description)
         print(example_items[i].src_example)
      else:
         if (0==i):
            print("no results found")
         break

def print_stats():
    print("number of examples: " + str(len(example_items)))

def load_all_sources():
   for s in source_files:
      load_examples(s)

def process_arguments():
   global max_num_of_print
   global search_terms

   if "--stat" == sys.argv[1]:
     if (2 == len(sys.argv)):
        print_stats()
     else:
        print("illegal numbert of arguments")
   else:
      i = 1
      while i < len(sys.argv):
         if "-n" == sys.argv[i]:
            i = i + 1
            max_num_of_print = int(sys.argv[i])
         else:
            search_terms.append(sys.argv[i])

         i = i + 1

      sort_examples()
      print_results()

load_all_sources()
process_arguments()
