$(document).ready(function(){
    $('#up').click(function(){
        $.post("/control_queue_add", {cmd: "up"});
    });
    $('#down').click(function(){
        $.post("/control_queue_add", {cmd: "down"});
    });
    $('#forwards').click(function(){
        $.post("/control_queue_add", {cmd: "forward"});
    });
    $('#backwards').click(function(){
        $.post("/control_queue_add", {cmd: "back"});
    });
    $('#turnLeft').click(function(){
        $.post("/control_queue_add", {cmd: "left"});
    });
    $('#turnRight').click(function(){
        $.post("/control_queue_add", {cmd: "right"});
    });
    $('#digFront').click(function(){
        $.post("/control_queue_add", {cmd: "dig"});
    });
    $('#digUp').click(function(){
        $.post("/control_queue_add", {cmd: "dig up"});
    });
    $('#digDown').click(function(){
        $.post("/control_queue_add", {cmd: "dig down"});
    });
});