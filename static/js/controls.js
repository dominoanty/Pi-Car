const LEFT = 37
const UP = 38
const RIGHT = 39
const DOWN = 40
const OTHER = 0

var map  = {38 : false, 37 : false, 40 : false, 39 : false}

let states = {"KEY1" : 1 , "KEY2" : 2, "KEY1KEY2":3, "DUMMY" : -1}

var textMap = {37: "left", 38 : "forward", 39 : "right", 40 : "backward"}

configFromKeys = function(key1, key2)
{
        text = [textMap[key1], textMap[key2]].join('_')

        if(text === "_")
            return "dummy"

        if (text.substr(0,1) == "_") 
            return text.substring(1);

        if (text.substr(text.length-1,1) == "_") 
            return text.substring(0,text.length-1);

        return text
        
}

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
                configString = configFromKeys(that.key1, that.key2)
                $.ajax({
                type: "POST",
                url: "/move/" + configString,
                success : function(response)
                        {
                                console.log("Received response " + response)

                        },
        
                });
            console.log("State is " + that.stateMgr.new_state + "and old state is " + that.stateMgr.old_state + " and key is " + that.key1 + " and " + that.key2)   
            $("#reporter").val("State is " + that.stateMgr.new_state)
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
            configString = configFromKeys(that.key1, that.key2)
            $.ajax({
                type: "POST",
                url: "/move/" + configString,
                success : function(response)
                        {
                                console.log("Received response " + response)

                        },
                
            });

            console.log("State is " + that.stateMgr.new_state + " and key is " + that.key1 + " and " + that.key2)   
            $("#reporter").text("State is " + that.stateMgr.new_state)   
        }
    }


}
let SMInstance = new StateMachine()

$( document ).keydown(SMInstance.onKeyDown);

$( document ).keyup(SMInstance.onKeyUp);




//----------nav btn clicks
$(document).on('mousedown touchstart', '.nav_btn', function(event){
    $(this).focus();
    let keycode = Number($(this).attr('data-keycode'));
    console.log(keycode+" was mousedown")    ;
    let e = $.Event('keydown');
    e.which = keycode;
    e.keyCode = keycode;
    $( document ).trigger(e);
});

$(".nav_btn").on('mouseup touchend', function(event){
    $(this).focus();
    let keycode = Number($(this).attr('data-keycode'));
    console.log(keycode+ " was mouseup");
    let e = $.Event('keyup');
    e.which = keycode;
    e.keyCode = keycode;
    $( document ).trigger(e);
});

