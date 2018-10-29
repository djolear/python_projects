// Chris - thanks for showing me how to decompose before section today. I didn't have time to change my code
//before I submitted it, but I do understand how to do it in the future! So thank you.

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include "console.h"
#include "filelib.h"
#include "simpio.h"
#include "strlib.h"
#include "vector.h"
using namespace std;

//prototype for madlibs function
Vector <string> single_madlib(string filename, int &individual_parameter_count, int &total_parameter_count, int &number_madlibs);

//main function
int main() {
    int total_parameter_count = 0; //initiate total number of parameters (added across all madlibs)
    int number_madlibs = 0; //initiate total number of madlibs finished (added across all madlibs)
    //welcome message
    cout << "Welcome to CS 106B Mad Libs!" << endl;
    cout << "I will ask you to provide various words" << endl;
    cout << "and phrases to fill in a story." << endl;
    cout << "At the end, I will display your story to you." << endl;
    cout << " " << endl;

    while (true) { //get name of input file from user until they give a name that exists
        string fn = getLine("Mad Lib input file?");
        while (!fileExists(fn)) {
            cout << "Unable to open that file.  Try again." << endl;
            fn = getLine("Mad Lib input file?");
        }
        cout << endl;
        int individual_parameter_count = 0; //initiate total number of parameters which RESETS AT 0 AFTER EACH MADLIB
        Vector <string> story = single_madlib(fn, individual_parameter_count, total_parameter_count, number_madlibs);//run madlib function
        cout << endl << "Your Madlib Story:" << endl;
        for (int i = 0; i < story.size(); i++) { //print out complete story, line by line
            cout << story[i] << endl;
        }
        cout << individual_parameter_count << " placeholder(s) replaced." << endl; //placeholder within specific madlib
        if (!getYesOrNo("Do another Mad Lib (Y/N)?", "Please type a word that starts with 'Y' or 'N'")) {
           break;
        }
    }

    cout << endl << "Mad Lib stories you created: " << number_madlibs << endl; //if done, total madlibs
    float average = total_parameter_count/number_madlibs; //if done, average number of parameters per madlib
    cout << "Total placeholders replaced: " << total_parameter_count << + " (" << fixed << setprecision(1) << average << " per story)"
         << endl;//tell user total madlibs & average parameter per madlib
        return 0;

}


Vector <string> single_madlib(string filename, int &individual_parameter_count, int &total_parameter_count, int &number_madlibs) {
    ifstream input;
    input.open(filename); //read in filename given in main
    string line;
    Vector <string> newtext; //initiate empty vector *ASK CHRIS IF THIS IS THE SAME AS THE STORY VECTOR IN MAIN
    while (getline(input, line)) {
        for (int i = 0; i <= line.size(); i++) { //for each line
            if (charToString(line[i]) == "<") { //if a "<" is found
               int stop = (line.find(">", i)) + 1; //try to find a ">"
               char check_for_next = line[stop]; //make sure there is a space before next "<"
               char check_for_prev = line[i-1]; //make sure there was a space before the identified "<"
               if (stop!=string::npos //if a ">" was found in the same line
                       && stop != 0 //and it didn't start the line back at 0 (which happens if stop is void? i don't understand this bug
                       //but this seems to fix it... maybe review in IGs?
                       && charToString(check_for_next) != "<" //and there aren't two parameters w/o a space, i.e., <noun><noun>
                       && charToString(check_for_prev) != ">") { //and there aren't two parameters w/o a space, i.e., <noun><noun>
                    string word = line.substr(i+1, line.substr(i).find(">") - 1); //save the parameter requested as var word
                        if(word[0] == 'a' || word[0] == 'e' || word[0] == 'i' || word[0] == 'o' || word[0] == 'u'||
                                word[0] == 'A' || word[0] == 'E' || word[0] == 'I' || word[0] == 'O' || word[0] == 'U') {
                            string ml = getLine("Please type an " + word + ":"); //if word starts w/vowel, ask user for this
                            //save their answer as string ml
                            line.replace(i, word.length() + 2, ml); //replace the index where the parameter request was found
                            //with the word the user gave
                            total_parameter_count++ ; //add 1 to total parameters performed
                            individual_parameter_count++ ; //add 1 to parameters performed within this function
                        }
                        if(word[0] != 'a' & word[0] != 'e' & word[0] != 'i' & word[0] != 'o' & word[0] != 'u'
                               & word[0] != 'A' & word[0] != 'E' & word[0] != 'I' & word[0] != 'O' & word[0] != 'U') {
                            string ml = getLine("Please type a " + word + ":");
                            line.replace(i, word.length() + 2, ml);
                            total_parameter_count++ ;
                            individual_parameter_count++ ; //same function but if the paramater ask starts w/consonant
                        }
               }
            }
        }
        newtext.add(line); //add adjusted line to the vector newtext
    }
    number_madlibs++ ; //add 1 to total madlibs solved
    input.close(); //close input
    return newtext; //return vector newtext
}




//Line breaks between lines for some txt files; was string, then vector, flips which are problematic.
//If starts with a vowel, put an "an" instead of "a" - faster way?
