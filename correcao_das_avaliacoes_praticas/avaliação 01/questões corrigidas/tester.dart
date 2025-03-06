import 'dart:io';
import 'dart:convert';

// DEBUG STUFF

void debugStringDiff(String a, String b) {
  print("=== DEBUG: Comparação de Strings ===");
  print("Saída Obtida: '${a.replaceAll("\n", "\\n")}'");
  print("Saída Esperada: '${b.replaceAll("\n", "\\n")}'");

  if (a.length != b.length) {
    print("🚨 As strings têm tamanhos diferentes! ${a.length} vs ${b.length}");
  }

  for (int i = 0; i < a.length && i < b.length; i++) {
    if (a[i] != b[i]) {
      print(
        "❌ Diferença no índice $i: '${a[i]}' vs '${b[i]}' (Código Unicode: ${a.codeUnitAt(i)} vs ${b.codeUnitAt(i)})",
      );
      break;
    }
  }
}

// GLOBAL VARIABLES

var DEBUG_MODE = false;
var VERBOSE_MODE = false;
var ONLY_DISPLAY_FINAL_RESULT = false;
var DISPLAY_ERRORS = true;

class TestCase {
  int number;
  bool correct = false;
  String input;
  String output;
  File pythonFile;

  TestCase(this.number, this.input, this.output, this.pythonFile);

  Future<bool> runTest() async {
    File pythonFile = this.pythonFile;
    String input = this.input;
    String expectedOutput = this.output;
    int timeoutSeconds = 2;

    Process process;
    try {
      process = await Process.start('python', [pythonFile.path]);
    } catch (e) {
      print("Erro ao iniciar o processo Python: $e");
      return false;
    }

    process.stdin.writeln(input);
    await process.stdin.flush();
    await process.stdin.close();

    Future<String> outputFuture = process.stdout.transform(utf8.decoder).join();
    Future<String> errorFuture =
        process.stderr.transform(latin1.decoder).join();
    Future<int> exitCodeFuture = process.exitCode;

    try {
      var results = await Future.wait([
        outputFuture,
        errorFuture,
        exitCodeFuture,
      ]).timeout(
        Duration(seconds: timeoutSeconds),
        onTimeout: () {
          process.kill(ProcessSignal.sigkill);
          return ["", "Timeout atingido", -1];
        },
      );

      String? output = results[0] as String?;
      String? errorOutput = results[1] as String?;
      int? exitCode = results[2] as int?;

      if (exitCode == -1) {
        print("⏳ Tempo limite atingido para ${pythonFile.path}");
        return false;
      }

      if (errorOutput!.isNotEmpty) {
        if (DISPLAY_ERRORS) {
          print("Erro Python: \n$errorOutput");
        }
        return false;
      }

      // NÃO TIRAR ESSA PARTE DO CÓDIGO NUNCA!
      // mais de 4 horas foram gastas aqui
      // o processo python retorna \r\n ao invés de \n
      // e a string de comparação dart apenas tem \n,
      //  isso é invisível no terminal e no debug console
      var treatedOutput = output!
          .trim()
          .replaceAll('\r\n', '\n')
          .replaceAll('\r', '');
      var treatedExpectedOutput = expectedOutput.trim().replaceAll(
        '\r\n',
        '\n',
      );
      if (VERBOSE_MODE && (treatedExpectedOutput != treatedOutput)) {
        print("Expected output:\n$treatedExpectedOutput");
        print("Output:\n$treatedOutput");
      }

      if (DEBUG_MODE) {
        debugStringDiff(treatedOutput, treatedExpectedOutput);
      }

      return treatedOutput == treatedExpectedOutput;
    } catch (e) {
      print("Erro inesperado: $e");
      return false;
    }
  }
}

class Subtask {
  String subtask;
  String questionNumber;
  File question;
  File input;
  File output;
  int totalTestCases = 0;
  int passedTestCases = 0;
  bool correct = false;

  Subtask(
    this.subtask,
    this.questionNumber,
    this.question,
    this.input,
    this.output,
  );

  List<String> groupByTripleNewlines(List<String> inputList) {
    List<String> result = [];
    List<String> tempGroup = [];

    for (var item in inputList) {
      if (item.isEmpty) {
        if (tempGroup.isNotEmpty) {
          result.add(tempGroup.join("\n"));
          tempGroup.clear();
        }
      } else {
        tempGroup.add(item);
      }
    }

    // Add last group if not empty
    if (tempGroup.isNotEmpty) {
      result.add(tempGroup.join("\n"));
    }

    return result;
  }

  List<TestCase> createTestCases() {
    var questionInputs = groupByTripleNewlines(input.readAsLinesSync());
    var questionOutputs = groupByTripleNewlines(output.readAsLinesSync());

    if (questionInputs.length != questionOutputs.length) {
      throw Exception("Mismatch between inputs and expected outputs!");
    }

    List<TestCase> testCases = [];

    for (int i = 0; i < questionInputs.length; i++) {
      testCases.add(
        TestCase(i, questionInputs[i], questionOutputs[i], question),
      );
    }

    totalTestCases = testCases.length;
    return testCases;
  }

  bool checkCompletion() {
    correct = (passedTestCases == totalTestCases);
    return correct;
  }
}

Future<List<Subtask>> loadTestCases() async {
  var scriptDir = File(Platform.script.toFilePath()).parent.parent;
  var testCasesDir = Directory(
    "${scriptDir.path}${Platform.pathSeparator}casos_de_teste",
  );

  var questionFiles = [
    File(
      "${scriptDir.path}${Platform.pathSeparator}gabarito${Platform.pathSeparator}questão0.py",
    ),
    File(
      "${scriptDir.path}${Platform.pathSeparator}gabarito${Platform.pathSeparator}questão1.py",
    ),
    File(
      "${scriptDir.path}${Platform.pathSeparator}gabarito${Platform.pathSeparator}questão2.py",
    ),
    File(
      "${scriptDir.path}${Platform.pathSeparator}gabarito${Platform.pathSeparator}questão3.py",
    ),
    File(
      "${scriptDir.path}${Platform.pathSeparator}gabarito${Platform.pathSeparator}questão4.py",
    ),
  ];

  List<Subtask> testCasesList = [];
  int i = -1;

  await for (var question in testCasesDir.list()) {
    if (question is! Directory) continue;
    i++;

    var subDirs = question.listSync().whereType<Directory>().toList();
    if (subDirs.length < 2) continue;

    var inputDir = subDirs[0];
    var outputDir = subDirs[1];

    List<File> subtaskInputs = inputDir.listSync().whereType<File>().toList();
    List<File> subtaskOutputs = outputDir.listSync().whereType<File>().toList();

    if (subtaskInputs.length != subtaskOutputs.length) {
      throw Exception("Mismatch in test case files!");
    }

    for (int c = 0; c < subtaskInputs.length; c++) {
      testCasesList.add(
        Subtask(
          subtaskInputs[c].uri.pathSegments.last,
          question.uri.pathSegments[question.uri.pathSegments.length - 2],
          questionFiles[i],
          subtaskInputs[c],
          subtaskOutputs[c],
        ),
      );
    }
  }

  return testCasesList;
}

Future<List<Subtask>> runTestCases(List<Subtask> questionsList) async {
  for (var question in questionsList) {
    var testCases = question.createTestCases();

    for (var testCase in testCases) {
      bool result = await testCase.runTest();
      if (result) {
        question.passedTestCases++;
        if (!ONLY_DISPLAY_FINAL_RESULT) {
          print(
            '✅ Passed: ${question.questionNumber} - ${question.subtask} - Test ${testCase.number}',
          );
        }
      } else {
        if (!ONLY_DISPLAY_FINAL_RESULT) {
          print(
            '❌ Failed: ${question.questionNumber} - ${question.subtask} - Test ${testCase.number}',
          );
        }
      }

      if (question.checkCompletion()) {
        print(
          '🎉 Question ${question.questionNumber} Subtask ${question.subtask} fully correct!',
        );
      }
    }
  }

  return questionsList;
}

void checkResults(List<Subtask> subtaskList) {
  for (var subtask in subtaskList) {
    if (subtask.correct) {
      print("✅ ${subtask.questionNumber} - ${subtask.subtask} - Passed (100%)");
    } else {
      double percentage =
          (subtask.passedTestCases / subtask.totalTestCases) * 100;
      print(
        "⚠️ ${subtask.questionNumber} - ${subtask.subtask} - Partially Passed ($percentage%)",
      );
    }
  }
}

void main(List<String> arguments) async {
  if (arguments.contains("--final")) {
    ONLY_DISPLAY_FINAL_RESULT = true;
  }
  if (arguments.contains("--noerror")) {
    DISPLAY_ERRORS = false;
  }
  if (arguments.contains("--verbose")) {
    VERBOSE_MODE = true;
  }
  if (arguments.contains("--debug")) {
    DEBUG_MODE = true;
  }
  if (arguments.contains("--help")) {
    print("""
      --help
        Print this
      
      --debug
        Display the string comparisson char by char

      --final
        Display the final result only.

      --noerror
        Don't display the python error ocurred in the subprocess

      --verbose
        Display the expected and actual output of each question
    """);
    exit(0);
  }

  var testCases = await loadTestCases();
  var questionList = await runTestCases(testCases);
  checkResults(questionList);
}
