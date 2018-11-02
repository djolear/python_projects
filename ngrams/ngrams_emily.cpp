// Name: Em Reit, SUID: emreit
// Problem Partner: Berk Can Deniz, SUID: bcdeniz

#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include "console.h"
#include "filelib.h"
#include "hashmap.h"
#include "map.h"
#include "simpio.h"
#include "strlib.h"
#include "random.h"
#include "set.h"
#include "hashset.h"
#include "lexicon.h"
using namespace std;

//Function protoypes.
Map<Vector<string>, Vector<string>> map_builder(Vector<string> story, int totalN);
void welcome();
string prompter_f();
int prompter_totalN();
Vector<string> reader(string filename);
void generate_jumble(int word_n, int totalN, Map<Vector<string>, Vector<string>> map_main);

//Prints out welcome message.
void welcome(){
    cout << "Welcome to CS 106B/X Random Writer ('N-Grams')!" << endl;
    cout << "This program generates random text based on a document." << endl;
    cout << "Give me an input file and an 'N' value for groups" << endl;
    cout << "of words, and I'll create random text for you." << endl;
    cout << "" << endl;
}

//Prompts user for file that exists.
string prompter_f(){
    string filename = getLine("Input file name?");
    while(!fileExists(filename)){
        cout << "Unable to open that file. Try again." << endl;
        filename = getLine("Input file name?");
    }
    return filename;
}

//Gets size of N-gram from user.
int prompter_totalN(){
    int totalN = getInteger("Value of N?");
    return totalN;
}

//Gets size of final story from user.
int prompter_w(){
    int word_n = getInteger("# of random words to generate (0 to quit)?");
    return word_n;
}

//Stores contents of file into a vector so that map_main can be built.
Vector<string> reader(string filename){
    ifstream input;
    input.open(filename);
    string word;
    Vector<string> story;
    while(input >> word){
        story.add(word);
    }
    return story;
}

//Builds a map with vector keys of N-1 words using the contents of story.
Map<Vector<string>, Vector<string>> map_builder(Vector<string> story, int totalN){
    Map<Vector<string>, Vector<string>> map_main;
    for(int i = 0; i < story.size(); i++){
        Vector <string> window;
        int end_point = i + totalN - 2;
        int new_val_index = i + totalN - 1;
        for (int j = i; j <= end_point; j++){
            window.add(story[j % story.size()]);
        }
        Vector <string> new_val;
        string word = story[new_val_index % story.size()];
        new_val.add(word);
        if(!map_main.containsKey(window)){
            map_main[window];
            map_main[window] = new_val;
        }
        else {
            Vector <string> vector_of_values = map_main.get(window);
            vector_of_values.add(word);
            map_main[window] = vector_of_values;
       }
    }
    return map_main;
}

//Takes as parameters length of total story (from user), size of N-gram, and the map above to generate random text.
void generate_jumble(int word_n, int totalN, Map<Vector<string>, Vector<string>> map_main){
    Vector <string> print_vector;
    Vector <Vector<string>> vector_of_keys = map_main.keys();
    int r = randomInteger(0, vector_of_keys.size() - 1);
    Vector <string> random_key = vector_of_keys[r];
    for(int k = 0; k < random_key.size(); k++){
        print_vector.add(random_key[k]);
    }
    while(print_vector.size() < word_n - totalN){
        Vector<string> vector_of_values = map_main[random_key];
        int r2 = randomInteger(0, vector_of_values.size() - 1);
        string next_word = vector_of_values[r2];
        print_vector.add(next_word);
        random_key.add(next_word);
        random_key.remove(0);
    }
    cout << "...";
    for (int j = 0; j < print_vector.size(); j ++) {
        cout << print_vector[j] << " ";
    }
    cout << "...";
    cout << endl;

}

//Main function runs the random text generator until user tells it to stop by entering 0.
int main() {
    ifstream input;
    welcome();
    string filename = prompter_f();
    int totalN = prompter_totalN();
    cout << " " << endl;
    while (true) {
        int word_n = prompter_w();
        if(word_n == 0){
            cout << "Exiting." << endl;
            break;
        } else {
            Vector<string> story = reader(filename);
            Map<Vector<string>, Vector<string> > map_main = map_builder(story, totalN);
            generate_jumble(word_n, totalN, map_main);
            cout << " " << endl;
        }
    }
    return 0;
}
