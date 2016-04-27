System.register(['./mock-cards', 'angular2/core'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var mock_cards_1, core_1;
    var CardService;
    return {
        setters:[
            function (mock_cards_1_1) {
                mock_cards_1 = mock_cards_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            }],
        execute: function() {
            CardService = (function () {
                function CardService() {
                }
                CardService.prototype.getCards = function () {
                    return Promise.resolve(mock_cards_1.CARDS);
                };
                CardService.prototype.getCard = function (id) {
                    return Promise.resolve(mock_cards_1.CARDS).then(function (cards) { return cards.filter(function (card) { return card.id === id; })[0]; });
                };
                CardService.prototype.getCardsSlowly = function () {
                    return new Promise(function (resolve) { return setTimeout(function () { return resolve(mock_cards_1.CARDS); }, 2000); });
                };
                CardService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [])
                ], CardService);
                return CardService;
            }());
            exports_1("CardService", CardService);
        }
    }
});
//# sourceMappingURL=card.service.js.map