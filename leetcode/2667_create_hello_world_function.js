var createHelloWorld = function (){
    /*
        This function return the phrase Hello World regardless of what is passed in. Different datatypes can be submitted but the function will still return hello world
    */
    return function(...args){
        return "Hello World";
    }
};