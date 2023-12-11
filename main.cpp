#include <vector>
#include <string>

std::vector<std::string> convert_args(int argc, char* argv[]) {
    std::vector<std::string> arguments;

    for (int i = 0; i < argc; ++i) {
        arguments.emplace_back(argv[i]);
    }

    return arguments;
}

int main(int argc, char* argv[]) {
	auto args = convert_args(argc, argv);

	
}