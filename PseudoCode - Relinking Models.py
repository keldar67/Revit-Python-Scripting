
# Get All of the Links

#For Each of the Links:

    #Get the Current Revision of this link
    
    #Get the Path and look in the folder to see if there is a higher revision
    
    #If there is a higher revision
    
        #Get that Revision
        
        #If the new Revision is Workshared 
            #Grab the current Worksets Closed from the current link and create a new WorksharedConfig Element
            
            
        #Else if not workshared
            #Add the model to the NotWorkshared List
            #Create a blank WorksharedConfig Element
        
        #Call the Relink with the new link and the Workshared Config Element
        
    #Else if not
    
        #Report that this is already current and up to date.