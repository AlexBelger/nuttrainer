System.register(['./mock-categories'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var mock_categories_1;
    var CARDS;
    return {
        setters:[
            function (mock_categories_1_1) {
                mock_categories_1 = mock_categories_1_1;
            }],
        execute: function() {
            exports_1("CARDS", CARDS = [
                { "id": 2, "category": mock_categories_1.CATEGORIES[0], "first": "Q1", "second": "A1" },
                { "id": 3, "category": mock_categories_1.CATEGORIES[1], "first": "Q2", "second": "A2" }
            ]);
        }
    }
});
//# sourceMappingURL=mock-cards.js.map