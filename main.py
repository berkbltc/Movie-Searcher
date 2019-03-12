
import file_parser
import search
import GUI

def search_word(word):
    return search.do_search(word)

if __name__ == "__main__":

    file_parser.parse_file("test-data.txt")
#    docsList=[]
#    app.run(host="localhost")
  
    GUI.vp_start_gui()    