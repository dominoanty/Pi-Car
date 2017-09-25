const LEFT = 37
const UP = 38
const RIGHT = 39
const DOWN = 40
const OTHER = 0

var map  = {38 : false, 37 : false, 40 : false, 39 : false}

let states = {"KEY1" : 1 , "KEY2" : 2, "KEY1KEY2":3, "DUMMY" : -1}


function StateManager(initState){
    this.old_state = initState;
    this.new_state = initState;
    let that = this;

    this.getCurrentState = function(){
        return that.new_state;
    }

    this.changeState = function(new_state){
        that.old_state = that.new_state;
        that.new_state = new_state;
    }
    
    this.hasStateChanged = function(){
        if(that.old_state == that.new_state)
            return false;
        else
            return true;
    }
}


function StateMachine(){
    this.key1 = null;
    this.key2 = null;
    this.stateMgr = new StateManager(states.DUMMY);
    var that = this

    this.onKeyDown = function(event){
        DIR = event.keyCode
        switch(that.stateMgr.getCurrentState())
        {
        case states.DUMMY: switch(DIR){
                                case UP: that.key1 = UP;
                                        that.stateMgr.changeState(states.KEY1);
                                        break;
                                case DOWN:that.key1 = DOWN;
                                        that.stateMgr.changeState(states.KEY1);
                                        break;
                                case LEFT: that.key2 = LEFT;
                                        that.stateMgr.changeState(states.KEY2);
                                        break;
                                case RIGHT: that.key2 = RIGHT;
                                            that.stateMgr.changeState(states.KEY2);
                                            break;
                                default: break;
                            }break;
                            
            
        case states.KEY2:  switch(DIR){
                                case UP: that.key1 = UP;
                                        that.stateMgr.changeState(states.KEY1KEY2);
                                        break;
                                case DOWN:that.key1 = DOWN;
                                        that.stateMgr.changeState(states.KEY1KEY2);
                                        break;
                                case LEFT: that.stateMgr.changeState(states.KEY2);break;
                                case RIGHT: that.stateMgr.changeState(states.KEY2);break;
                                default: break;
                            }break;
            
        case states.KEY1: switch(DIR){
                                case UP: that.stateMgr.changeState(states.KEY1);break;
                                case DOWN: that.stateMgr.changeState(states.KEY1);break;
                                case LEFT: that.key2 = LEFT;
                                        that.stateMgr.changeState(states.KEY1KEY2);
                                        break;
                                case RIGHT:that.key2 = RIGHT;
                                        that.stateMgr.changeState(states.KEY1KEY2);
                                        break;
                                default: break;
                            }break;
        case states.KEY1KEY2 : 
                            if(DIR == that.key1 || DIR == that.key2)
                                    that.stateMgr.changeState(states.KEY1KEY2)
                            break;
        }
        if(that.stateMgr.hasStateChanged())
        {
            console.log("State is " + that.stateMgr.new_state + "and old state is " + that.stateMgr.old_state + " and key is " + that.key1 + " and " + that.key2)   
        }
        
    }


    this.onKeyUp = function(event){
        DIR = event.keyCode
        switch(that.stateMgr.getCurrentState()){
            case states.KEY1KEY2:switch(DIR){
                                case UP: that.key1 = null;
                                        that.stateMgr.changeState(states.KEY2);
                                        break;
                                case DOWN:that.key1 = null;
                                        that.stateMgr.changeState(states.KEY2);
                                        break;
                                case LEFT: that.key2 = null;
                                        that.stateMgr.changeState(states.KEY1);
                                        break;
                                case RIGHT: that.key2 = null;
                                            that.stateMgr.changeState(states.KEY1);
                                            break;
                                default: break;
                            }break;
            
            case states.KEY1:switch(DIR){
                                case UP: that.key1 = null;
                                        that.stateMgr.changeState(states.DUMMY);
                                        break;
                                case DOWN:that.key1 = null;
                                        that.stateMgr.changeState(states.DUMMY);
                                        break;
                                case LEFT: that.stateMgr.changeState(states.LEFT);break;
                                case RIGHT: that.stateMgr.changeState(states.RIGHT);break;
                                default: break;
                            }break;
            
            case states.KEY2:switch(DIR){
                                case UP: that.stateMgr.changeState(states.UP);break;
                                case DOWN: that.stateMgr.changeState(states.DOWN);break;
                                case LEFT: that.key2 = null;
                                        that.stateMgr.changeState(states.DUMMY);
                                        break;
                                case RIGHT:that.key2 = null;
                                        that.stateMgr.changeState(states.DUMMY);
                                        break;
                                default: break;
                            }break;
            case states.DUMMY:
                            that.stateMgr.changeState(states.DUMMY);break;
        }
        if(that.stateMgr.hasStateChanged())
        {
            console.log("State is " + that.stateMgr.new_state + " and key is " + that.key1 + " and " + that.key2)   
        }
    }


}
let SMInstance = new StateMachine()

document.addEventListener('keydown', SMInstance.onKeyDown );

document.addEventListener('keyup', SMInstance.onKeyUp);

