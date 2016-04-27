System.register(['angular2/router', 'angular2/core', './card.service'], function(exports_1, context_1) {
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
    var router_1, core_1, card_service_1;
    var CardsComponent;
    return {
        setters:[
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (card_service_1_1) {
                card_service_1 = card_service_1_1;
            }],
        execute: function() {
            CardsComponent = (function () {
                function CardsComponent(_cardService, _router) {
                    this._cardService = _cardService;
                    this._router = _router;
                    this.title = 'Latest additions';
                }
                CardsComponent.prototype.ngOnInit = function () {
                    this.getCards();
                };
                CardsComponent.prototype.gotoCard = function (card) {
                    var link = ['Card', { id: card.id }];
                    this._router.navigate(link);
                };
                CardsComponent.prototype.getCards = function () {
                    var _this = this;
                    this._cardService.getCardsSlowly().then(function (cards) { return _this.cards = cards; });
                };
                CardsComponent = __decorate([
                    core_1.Component({
                        selector: 'cards',
                        template: "\n        <h1>{{title}}</h1>\n\t<hr/>\n\t<ul class=\"cards\">\n        <li *ngFor=\"#card of cards\"\n            (click)=\"gotoCard(card)\">\n\t<span class=\"badge\">{{card.category.name}}</span> - {{card.first}}\n        </li>\n\t</ul>\n\t<hr/>\n        ",
                        styles: ["\n  .selected {\n    background-color: #CFD8DC !important;\n    color: white;\n  }\n  .cards {\n    margin: 0 0 2em 0;\n    list-style-type: none;\n    padding: 0;\n    width: 15em;\n  }\n  .cards li {\n    cursor: pointer;\n    position: relative;\n    left: 0;\n    background-color: #EEE;\n    margin: .5em;\n    padding: .3em 0;\n    height: 1.6em;\n    border-radius: 4px;\n  }\n  .cards li.selected:hover {\n    background-color: #BBD8DC !important;\n    color: white;\n  }\n  .cards li:hover {\n    color: #607D8B;\n    background-color: #DDD;\n    left: .1em;\n  }\n  .cards .text {\n    position: relative;\n    top: -3px;\n  }\n  .cards .badge {\n    display: inline-block;\n    font-size: small;\n    color: white;\n    padding: 0.8em 0.7em 0 0.7em;\n    background-color: #607D8B;\n    line-height: 1em;\n    position: relative;\n    left: -1px;\n    top: -4px;\n    height: 1.8em;\n    margin-right: .8em;\n    border-radius: 4px 0 0 4px;\n  }\n\t    "]
                    }), 
                    __metadata('design:paramtypes', [card_service_1.CardService, router_1.Router])
                ], CardsComponent);
                return CardsComponent;
            }());
            exports_1("CardsComponent", CardsComponent);
        }
    }
});
//# sourceMappingURL=cards.component.js.map