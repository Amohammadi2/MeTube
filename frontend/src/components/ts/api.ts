import { writable, get} from "svelte/store";
import axios from "axios";
import { apiUrl } from "./states";
import type { INotification } from "./interfaces";

export const APIRequest = axios.create({
    baseURL: apiUrl,
})

export class Notifications {

    public static _notifications = writable(<Array<INotification>>[]); 

    public states: object = {
        error: "rgb(211, 17, 50)",
        success: "rgb(28, 180, 79)",
        warning: "rgb(204, 180, 41)",
    };

    private _show_notification(message:string, state: string) {
        if (!(state in this.states)) this._show_notification(`${state} doesn't exist in states`, "error");
        // // Todo: implement this method to abstract out adding notifications
        Notifications._notifications.update(value => {
            value.push(<INotification> {
                message, state
            });
            return value;
        })
    }

    public error (msg: string):void {
        // // Todo: implement this
        this._show_notification(msg, "error");
    }

    public warning(msg: string):void {
        // // Todo: implement this
        this._show_notification(msg, "warning");
    }

    public success(msg: string):void {
        // // Todo: implement this
        this._show_notification(msg, "success");
    }

    /**
     * a custom event handler for notifications
     * it clears notifications on `click` event
     */
    public static close (event: MouseEvent) {
        let message: string = (<HTMLElement>event.target).innerText; 
        Notifications._notifications.update(value => {
            for (let index in value){
                if (value[index].message == message) {
                    // becaue the type of index is string I used `+` before
                    // its name to convert it into a number
                    value.splice(+index, 1);
                }
            }
            return value;
        })
    }
}