class BoggleGame {
    constructor(boardId){

        this.board = $(`#${boardId}`);
        this.words = new Set();
        this.score = 0;
        
        $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
    }

}

    showWord(word) {
        $(".words", this.board).append($("<li>", { text: word }));
    }

    async handleSubmit(e) {
        e.preventDefault();
        const $word = $(".word", this.board);

        let word = $word.val();
        if (!word) return;

        if (this.words.has(word)) {
            this.showMessage(`Already found ${word}`, "err");
            return;
        }
    }
