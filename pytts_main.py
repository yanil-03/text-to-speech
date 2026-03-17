import pyttsx3 
import os 
import sys 

def main() -> None:
    try:
        output_dir = "output"
        os.makedirs(output_dir,exist_ok=True) 
        
        engine = pyttsx3.init() 
        
        voices=engine.getProperty("voices") 
        
        if(len(voices)> 1 ):
            engine.setProperty("voices",voices[1].id) 
        else:
            engine.setProperty("voices",voices[0].id) 
        
        engine.setProperty("rate",170) 
        
        engine.setProperty("volume",1.0) 
        
        text = "Hello Mehul , this audio is saved offline using pyttsx3" 
        
        output_path = os.path.join(output_dir,"pyttsx3_output.mp3") 
        
        engine.save_to_file(text,output_path) 
        
        engine.runAndWait() 
        
        print("File saved {output_path}") 
        
    except Exception as e:
        print("Error !",e)
        sys.exit(1) 
        
if __name__=="__main__":
    main()