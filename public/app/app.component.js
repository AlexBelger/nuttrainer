System.register(['angular2/core', 'angular2/router', './category.service', './card.service', './cards.component', './card.component'], function(exports_1, context_1) {
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
    var core_1, router_1, category_service_1, card_service_1, cards_component_1, card_component_1;
    var AppComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (category_service_1_1) {
                category_service_1 = category_service_1_1;
            },
            function (card_service_1_1) {
                card_service_1 = card_service_1_1;
            },
            function (cards_component_1_1) {
                cards_component_1 = cards_component_1_1;
            },
            function (card_component_1_1) {
                card_component_1 = card_component_1_1;
            }],
        execute: function() {
            AppComponent = (function () {
                function AppComponent(_categoryService) {
                    this._categoryService = _categoryService;
                    this.catInit = [
                        { "id": 0, "name": "All" },
                        { "id": 1, "name": "Unspecified" }
                    ];
                }
                AppComponent.prototype.ngOnInit = function () {
                    this.getCategories();
                    this.selectedCategory = this.catInit[0];
                    this.categories = this.catInit;
                };
                AppComponent.prototype.onSelect = function (category) {
                    this.selectedCategory = category;
                };
                AppComponent.prototype.getCategories = function () {
                    var _this = this;
                    this._categoryService.getCategories().then(function (categories) { return _this.categories.push.apply(_this.categories, categories); });
                };
                AppComponent = __decorate([
                    core_1.Component({
                        selector: 'app',
                        template: "\n\t<select [(ngModel)]=\"selectedCategory\">\n        <option *ngFor=\"#category of categories\" [ngValue]=\"category\">{{category.name}}</option>\n        </select>\n\t<nav>\n\t<a [routerLink]=\"['Cards']\">Cards</a>\n\t<a [routerLink]=\"['Newcard']\">Add Card</a>\n\t</nav>\n\t<router-outlet></router-outlet>\n\t",
                        directives: [router_1.ROUTER_DIRECTIVES],
                        providers: [
                            router_1.ROUTER_PROVIDERS,
                            card_service_1.CardService,
                            category_service_1.CategoryService
                        ]
                    }),
                    router_1.RouteConfig([
                        {
                            path: '/cards',
                            name: 'Cards',
                            component: cards_component_1.CardsComponent
                        },
                        {
                            path: '/card',
                            name: 'Newcard',
                            component: card_component_1.CardComponent
                        },
                        {
                            path: '/card/:id',
                            name: 'Card',
                            component: card_component_1.CardComponent
                        }
                    ]), 
                    __metadata('design:paramtypes', [category_service_1.CategoryService])
                ], AppComponent);
                return AppComponent;
            }());
            exports_1("AppComponent", AppComponent);
        }
    }
});
//# sourceMappingURL=app.component.js.map