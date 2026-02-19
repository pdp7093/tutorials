import { Component,useState,markup} from "@odoo/owl";
import {Counter} from "./counter/counter"
import {Card} from "./card/card";
import {TodoList} from "./todo/todo_list";
export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = {Counter,Card,TodoList};
    
    setup(){
        this.safeHtml = markup("<strong> This is bold HTML </strong>");
        this.normalHtml = "<strong>This will not be bold</strong>"
        
        this.state = useState({ sum:  0});
    }
   incrementSum = () => {
    this.state.sum++;
};
}