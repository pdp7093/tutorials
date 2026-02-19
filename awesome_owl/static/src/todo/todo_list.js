import { Component, useState, useRef, onMounted } from "@odoo/owl";
import { TodoItem } from "./todo_item";

export class TodoList extends Component {
    static template = "awesome_owl.TodoList";
    static components = { TodoItem };

    setup() {
        this.todos = useState([]);
        this.nextId =1;

        this.inputRef = useRef("input");

        onMounted(() => {
            this.inputRef.el.focus();
        });
    }
    addTodo(ev){
        if(ev.keyCode===13){
            const value = ev.target.value.trim();

            if(!value){
                return;
            }

            this.todos.push({
                id:this.nextId++,
                description:value,
                isCompleted:false,
            });

            ev.target.value="";

        }

    }
    toggleTodo = (id) => {
        const todo = this.todos.find(t => t.id === id);
        if (todo) {
            todo.isCompleted = !todo.isCompleted;
        }
    };

   deleteTodo = (id) => {
        const index = this.todos.findIndex(t => t.id === id);
        if (index !== -1) {
            this.todos.splice(index, 1);
        }
    };

}
