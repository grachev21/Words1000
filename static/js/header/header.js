import Tools from "../Tools.js";

class Header {
    constructor() {
        this.tools = new Tools();
        this.dropDownMenu()
    }
    dropDownMenu() {
        this.tools.actionOpenClose("click", "drop-down-menu", "button-header-menu")
    }
}
export default Header;
