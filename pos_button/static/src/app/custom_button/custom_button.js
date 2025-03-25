import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";

patch(ControlButtons.prototype, {
    async onClickPopupSingleField() {
        if (!this.env || !this.env.services || !this.env.services.action) {
            console.error("Action service is not available");
            return;
        }

        // Debugging
        console.log("Navigating to Repair Order");

        // Redirect to Repair Order Form
        this.env.services.action.doAction({
            type: 'ir.actions.act_window',
            res_model: 'repair.order',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'current',
        });
    }
});
