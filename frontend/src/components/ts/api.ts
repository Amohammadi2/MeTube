import { writable, get} from "svelte/store";
import axios from "axios";
import { apiUrl } from "./states";
import type { INotification } from "./interfaces";

export const APIRequest = axios.create({
    baseURL: apiUrl,
})

export class Notifier {

    public static _notifications = writable(<Array<INotification>>[]); 

    public states: object = {
        error: "rgb(211, 17, 50)",
        success: "rgb(28, 180, 79)",
        warning: "rgb(204, 180, 41)",
    };

    private _show_notification(message:string, state: string) {
        if (!(state in this.states)) this._show_notification(`${state} doesn't exist in states`, "error");
        // // Todo: implement this method to abstract out adding notifications
        Notifier._notifications.update(value => {
            value.push(<INotification> {
                message, state, key: Symbol(),
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
    public static close (event: MouseEvent, key: symbol) {
        console.log(key);
        Notifier._notifications.update(value => {
            return value.filter((value, index, array) => {
                if (value.key != key) {
                    return value;
                }
            });
        });
    }
}