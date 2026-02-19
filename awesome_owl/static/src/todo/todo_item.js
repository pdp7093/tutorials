import { Component } from "@odoo/owl";
import { Card } from "../card/card";
export class TodoItem extends Component {
    static template = "awesome_owl.TodoItem";
    static Component = {Card};
    static props = {
        todo:Object,
        onToggle:Function,
        onDelete:Function,
    };
    toggle(){
        this.props.onToggle(this.props.todo.id);
    }
    delete(){
        this.props.onDelete(this.props.todo.id)
    }
}