var AppMessage = angular.module('messageApp', ['ngResource']);


AppMessage.factory("restApis", function ($resource, $cacheFactory) {

    return {
        Message: $resource('/api/v1/message/', {}, {
            query: {method: "GET", cache: $cacheFactory, isArray: true},
            create: { method: "POST" }
        })
    };
});


AppMessage.controller("MessageList", function ($scope, restApis, $attrs) {

    if ($attrs.id == "Message") {
        restApis.Message.query(function (data) {
            $scope.messages = data;

        });
    }
});





